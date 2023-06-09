import numpy as np


class ZygoXYZReader:
    def __init__(self, filename: str):
        """Initialize ZygoXYZReader with filename

        Args:
            filename (str): filename
        """
        with open(filename, "r") as f:
            self.lines = f.readlines()

        self._parse_header()
        self._parse_data()

    def _parse_header(self):
        """Parse header in file based on ASCII Data File Header format
        Please refer P449 in https://www.seas.upenn.edu/~nanosop/documents/MetroProReferenceGuide0347_M.pdf
        """
        (
            self.intens_origin_x,
            self.intens_origin_y,
            self.intens_width,
            self.intens_height,
            self.n_buckets,
            self.intens_range,
        ) = map(float, self.lines[2][:-1].split(" "))

        (
            self.phase_origin_x,
            self.phase_origin_y,
            self.phase_width,
            self.phase_height,
        ) = map(float, self.lines[3][:-1].split(" "))

        (
            self.source,
            self.intf_scale_factor,
            self.wave_length_in,
            self.numerical_aperture,
            self.obliquity_factor,
            self.magnification,
            self.camera_res,
            self.time_stamp,
        ) = map(float, self.lines[7][:-1].split(" "))

        (
            self.camera_width,
            self.camera_height,
            self.system_type,
            self.system_board,
            self.system_serial,
            self.instrument_id,
            self.objective_name,
        ) = map(float, self.lines[8][:-1].split(" "))
        
        (
            self.acquire_mode,
            self.intens_avg,
            self.PZT_cal,
            self.PZT_gain,
            self.PZT_gain_tolerance,
            self.AGC,
            self.target_range,
            self.light_level,
            self.min_mod,
            self.min_mod_pts,
        ) = map(float, self.lines[9][:-1].split(" "))
        
        (
            self.phase_res,
            self.phase_avgs,
            self.minimum_area_size,
            self.discon_action,
            self.discon_filter,
            self.connection_order,
            self.remove_tilt_bias,
            self.data_sign,
            self.code_v_type,
        ) = map(float, self.lines[10][:-1].split(" "))
        
        self.refractive_index, self.part_thickness = map(
            float, self.lines[12][:-1].split(" ")
        )
        
        self.zoom_desc = map(float, self.lines[13][:-1].split(" "))

    def _parse_data(self):
        """Parse data in file"""
        x_list = []
        y_list = []
        z_list = []

        for line in self.lines[14:]:
            splitted = line[:-1].split(" ")
            if len(splitted) == 3:
                y_list.append(float(splitted[0]))
                x_list.append(float(splitted[1]))
                z_list.append(float(splitted[2]))
            elif len(splitted) == 4:
                y_list.append(float(splitted[0]))
                x_list.append(float(splitted[1]))
                z_list.append(np.nan)

        x_list = np.array(x_list)
        y_list = np.array(y_list)
        z_list = np.array(z_list)

        self.x_len = int(np.max(x_list) + 1)
        self.y_len = int(np.max(y_list) + 1)

        self.x_grid = x_list.reshape((y_len, x_len))
        self.y_grid = y_list.reshape((y_len, x_len))
        self.z_grid = z_list.reshape((y_len, x_len))
