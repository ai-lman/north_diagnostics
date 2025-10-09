import nptdms
import numpy as np

def read_probe_data(path, shot, channel):
    """
    Reads probe data for a single channel or multiple channels from TDMS files.
    
    Parameters:
        path (str): Base path to the data files.
        shot (int): Shot number.
        channel (int|str|list): Channel number(s) to read from (e.g., 16, "16", or [16, 17, 18]).
    
    Returns:
        Tuple:
            - t_bias (np.array): Time array in seconds
            - V_bias (np.array or None): Bias voltage (same for all probes)
            - I_probe (np.array for single channel, or dict for multiple)
    """
    try:
        # Constants
        fct = 20 / (2**16 - 1)

        # Load TDMS file once
        tdms_file = nptdms.TdmsFile.read(f"{path}/ddaq{shot}.tdms")
        data_group = tdms_file['data']

        # Time and bias voltage
        t_bias = data_group["ch2"][:]
        t_bias = np.arange(t_bias.size) * 1e-6  # s

        V_bias = data_group["ch7"][:] * fct * 11.75  # V

        # Handle single or multiple channels
        if isinstance(channel, (int, str)):
            ch_str = str(channel)
            I_probe = data_group[f"ch{ch_str}"][:] * fct / 213  # A
            return t_bias, V_bias, I_probe

        elif isinstance(channel, list):
            I_dict = {}
            for ch in channel:
                ch_str = str(ch)
                try:
                    I_data = data_group[f"ch{ch_str}"][:] * fct / 213
                    I_dict[int(ch)] = I_data
                except KeyError:
                    print(f"⚠️ Channel ch{ch_str} not found in shot {shot}")
            return t_bias, V_bias, I_dict
        
        else:
            raise ValueError("`channel` must be an int, str, or list of those.")

    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
        return None, None, None
