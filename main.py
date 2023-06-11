SEGMENT_LENGTH = 4
OVERLAP_LENGTH = 3
RESULT_MIN_LENGTH = 7
RESULT_MAX_LENGTH = 9


def run():
    # TODO: REPL

    inputs = get_inputs()
    segments = generate_segments(inputs)
    segment_map = generate_segment_map(segments)
    results = generate_results(inputs, segments, segment_map)

    write_outputs(results)


def write_outputs(results):
    with open("outputs.txt", "w") as outputs_file:
        outputs_file.writelines([f"{word}\n" for word in sorted(results)])


def get_inputs():
    inputs = []
    with open("inputs.txt") as inputs_file:
        file_lines = inputs_file.readlines()
        for line in file_lines:
            formatted_line = line.strip()
            if len(formatted_line):
                inputs.append(formatted_line)
    return inputs


def generate_results(inputs, segments, segment_map):
    working_queue = list(segments)
    results = set()

    while len(working_queue):
        working_item = working_queue.pop(0)
        item_end = working_item[-OVERLAP_LENGTH:]
        if item_end in segment_map:
            for next_part in segment_map[item_end]:
                result = f"{working_item}{next_part[OVERLAP_LENGTH:]}"
                if (
                    RESULT_MIN_LENGTH <= len(result) <= RESULT_MAX_LENGTH
                    and result not in inputs
                ):
                    results.add(result)
                if len(result) < RESULT_MAX_LENGTH:
                    working_queue.append(result)
    return results


def generate_segment_map(segments):
    segment_map: dict[str, list[str]] = {}
    for segment in segments:
        if segment[:OVERLAP_LENGTH] in segment_map:
            segment_map[segment[:OVERLAP_LENGTH]].append(segment)
        else:
            segment_map[segment[:OVERLAP_LENGTH]] = [segment]
    return segment_map


def generate_segments(_inputs):
    segments = set()
    for word in _inputs:
        for character_index in range(len(word)):
            segmentation_start = SEGMENT_LENGTH - 1
            if character_index >= segmentation_start:
                segment_start = character_index - segmentation_start
                segment_end = character_index + 1
                segments.add(word[segment_start:segment_end])
    return segments


if __name__ == "__main__":
    run()
