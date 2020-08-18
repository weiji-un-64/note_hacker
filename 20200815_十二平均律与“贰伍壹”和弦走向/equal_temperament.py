"""
@Author: MaraPapMann
@Copyright: MaraPapMann
Please do not use it for any commercial purpose.
"""
import winsound


def get_equal_temperament_scale(init_freq):
    """
    :param init_freq: Initial frequency, e.g. A = 440 Hz
    :return: equal_temperament_scale_lst: a list containing 12 Notes in an octave derived by equal temperament
    """

    # Initialization
    equal_temperament_scale_lst = [init_freq]  # Creating a list
    q = 2 ** (1 / 12)  # The pre-defined ratio
    n = 12  # 12 notes in 1 octave

    # Computing the list
    for i in range(1, n):
        init_freq = init_freq * q
        equal_temperament_scale_lst.append(init_freq)

    return equal_temperament_scale_lst


def round_lst(equal_temperament_scale_lst):
    """
    :param equal_temperament_scale_lst: a list containing 12 Notes in an octave derived by equal temperament
    :return: rounded_scale_lst: a rounded scale for winsound input
    """

    # Initialization
    rounded_scale_lst = []  # Creating a list

    # Rounding
    for freq in equal_temperament_scale_lst:
        rounded_scale_lst.append(int(freq))  # Round each frequency in the list

    return rounded_scale_lst


if __name__ == '__main__':
    init_freq = 440  # Initial frequency 440 Hz, please temper it as you wish
    note_name_lst = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]  # Hard-coded Note Name

    equal_temperament_scale_lst = get_equal_temperament_scale(init_freq)

    # Print the name of the note and its frequency
    for i in range(len(equal_temperament_scale_lst)):
        print(note_name_lst[i] + ": " + str(equal_temperament_scale_lst[i]) + " Hz")

    # Round the floats to integers
    rounded_scale_lst = round_lst(equal_temperament_scale_lst)

    # Make the noise
    for freq in rounded_scale_lst:
        winsound.Beep(freq, 1000)
