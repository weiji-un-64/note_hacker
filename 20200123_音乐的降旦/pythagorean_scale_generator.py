"""
@Author: MaraPapMann
@Copyright: MaraPapMann
Please do not use it for any commercial purpose.
"""
import winsound


def get_pythagorean_scale(init_freq):
    """
    @param: double % init_freq: Initial frequency, for further computation of the pythagorean scale.
    @return: list % ptg_scale: Pythagorean Scale, for tuning the winsound.Beep function.
    """
    n_itr = 6  # Number of iteration, set to 6, for there are totally 13 notes in one octave,
    # including the head and tail.

    # Computing the ascending pythagorean scale.
    ascd_ptg_scale = [init_freq]
    for i in range(n_itr):
        cur_freq = ascd_ptg_scale[i]  # Switching to the frequency to be used.
        next_freq = (cur_freq * 3) / 2  # Computing the next frequency.
        next_freq = check_in_octave(init_freq,
                                    next_freq)  # Check whether the frequency is in this octave. If not, edit it.
        ascd_ptg_scale.append(next_freq)  # Push it into the list

    # Computing the descending pythagorean scale.
    dscd_ptg_scale = [init_freq]
    for i in range(n_itr):
        cur_freq = dscd_ptg_scale[i]  # Switching to the frequency to be used.
        next_freq = (cur_freq * 2) / 3  # Computing the next frequency.
        next_freq = check_in_octave(init_freq,
                                    next_freq)  # Check whether the frequency is in this octave. If not, edit it.
        dscd_ptg_scale.append(next_freq)  # Push it into the list.

    # Merging the two lists into one and thereafter sorting it in an ascending order.
    ptg_scale = list(set(ascd_ptg_scale) | set(dscd_ptg_scale))  # Getting rid of duplicates.
    ptg_scale.sort()  # Sorting it in an ascending order.

    return ptg_scale


def check_in_octave(init_freq, freq):
    """
    @param: double % init_freq: Initial frequency.
    @param: double % freq: Current input frequency.
    @return: double % freq: Processed frequency.
    """
    while freq >= init_freq * 2 or freq <= init_freq:
        if freq >= init_freq * 2:  # If this frequency is higher than this octave,
            freq = freq / 2  # Divide it by 2.
        else:  # If this frequency is lower than this octave,
            freq = freq * 2  # Multiply it by 2.
    freq = int(freq)  # Frequency must be integer so that it can be input in to the Beep function.
    return freq


if __name__ == '__main__':
    input_freq = 440  # This is the input frequency. Please adjust it as you wish.
    ptg_scale = get_pythagorean_scale(input_freq)
    for freq in ptg_scale:
        winsound.Beep(freq, 1000)
