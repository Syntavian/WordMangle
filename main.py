SEGMENT_LENGTH = 2

inputs = ["doctor", "acrobat", "caravan", "police", "avalanche", "violence"]


def run():
    # TODO: REPL

    # TODO: Validate inputs

    segments = generate_segments(inputs)

    print(segments)

    # TODO: Generate outputs


def generate_segments(_inputs):
    segments = []
    for word in _inputs:
        for character_index in range(len(word)):
            segmentation_start = SEGMENT_LENGTH - 1
            if character_index >= segmentation_start:
                segment_start = character_index - segmentation_start
                segment_end = character_index + 1
                segments.append(word[segment_start:segment_end])
    return segments


if __name__ == "__main__":
    run()
