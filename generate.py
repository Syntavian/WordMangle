from config import *


def generate(_inputs=[]):
    segments, start_segments, end_segments = generate_segments(_inputs)
    segment_map = generate_segment_map(segments)
    results = generate_results(_inputs, start_segments, end_segments, segment_map)
    sorted_results = sorted(results)

    print_outputs(sorted_results)
    write_outputs(sorted_results)


def print_outputs(_results):
    print()

    for i in range(0, len(_results), 5):
        print(*_results[i : i + 5])

    print()


def write_outputs(_results=[]):
    with open(OUTPUT_FILE_NAME, "w") as outputs_file:
        outputs_file.writelines([f"{word}\n" for word in _results])


def get_inputs():
    inputs = set()

    with open(INPUT_FILE_NAME) as inputs_file:
        file_lines = inputs_file.readlines()

        for line in file_lines:
            formatted_line = line.strip()

            if len(formatted_line):
                inputs.add(formatted_line)

    return inputs


def generate_results(_inputs, _start_segments, _end_segments, _segment_map):
    working_queue = list(_start_segments)
    results = set()

    while len(working_queue):
        working_item = working_queue.pop(0)
        item_end = working_item[-OVERLAP_LENGTH:]

        if item_end in _segment_map:
            for next_part in _segment_map[item_end]:
                result = f"{working_item}{next_part[OVERLAP_LENGTH:]}"

                if (
                    RESULT_MIN_LENGTH <= len(result) <= RESULT_MAX_LENGTH
                    and result not in _inputs
                    and result[-SEGMENT_LENGTH:] in _end_segments
                ):
                    results.add(result)

                if len(result) < RESULT_MAX_LENGTH:
                    working_queue.append(result)

    return results


def generate_segment_map(_segments):
    segment_map: dict[str, list[str]] = {}

    for segment in _segments:
        if segment[:OVERLAP_LENGTH] in segment_map:
            segment_map[segment[:OVERLAP_LENGTH]].append(segment)
        else:
            segment_map[segment[:OVERLAP_LENGTH]] = [segment]

    return segment_map


def generate_segments(_inputs):
    segments = set()
    start_segments = set()
    end_segments = set()

    for word in _inputs:
        for character_index in range(len(word)):
            segmentation_start = SEGMENT_LENGTH - 1

            if character_index >= segmentation_start:
                segment_start = character_index - segmentation_start
                segment_end = character_index + 1
                segment = word[segment_start:segment_end]
                segments.add(segment)

                if character_index == segmentation_start:
                    start_segments.add(segment)

                if character_index == len(word) - 1:
                    end_segments.add(segment)

    return segments, start_segments, end_segments


if __name__ == "__main__":
    inputs = get_inputs()

    generate(inputs)
