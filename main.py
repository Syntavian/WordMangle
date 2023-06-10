SEGMENT_LENGTH = 3
OVERLAP_LENGTH = 2

inputs = ["doctor", "acrobat", "caravan", "police", "avalanche", "violence"]


def run():
    # TODO: REPL

    # TODO: Validate inputs

    segments = generate_segments(inputs)

    print(segments)

    segment_map = generate_segment_map(segments)

    print(segment_map)

    # TODO: Generate outputs


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
