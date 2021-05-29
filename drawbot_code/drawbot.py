import time

import hatched
import numpy as np
import serial
import tqdm

from optimize import optimize_ordering
from preview import preview_drawing
from utils import *


from shapely.geometry import MultiLineString


#############
# Constants #
#############

STEPS_PER_MM = 20
WIDTH_MM = 62
HEIGHT_MM = 225
WIDTH_STEPS = WIDTH_MM * STEPS_PER_MM
HEIGHT_STEPS = HEIGHT_MM * STEPS_PER_MM


def main():
    # Get lines to draw
    print('Converting image to lines...', end='', flush=True)
    # Some pretuned images and parameters as examples
    params = [
        dict(file_path='imgs/skull.png',
             hatch_pitch=5,
             levels=(24, 80, 128),
             blur_radius=15,
             invert=True),
        dict(file_path='imgs/lines.jpg',
             hatch_pitch=4,
             levels=(240, 240, 240),
             blur_radius=0),
        dict(file_path='imgs/lenna.png',
             hatch_pitch=2,
             levels=(102, 148, 200),
             blur_radius=8),
        dict(file_path='imgs/helloworld.png',
             hatch_pitch=5,
             levels=(24, 80, 130),
             blur_radius=15,
             invert=True)
    ]

    # Converts an image to line drawing with diagonal hatching
    # Play with levels parameter and blurring to get right
    # Will error if contours too complicated
    mls = hatched.hatch(**params[3], save_svg=False, show_plot=False)

    mls = mls_normalize(mls) # put lines in unit square
    lines = list(mls_to_lines(mls)) # convert to simple list of list of points

    # Greedily sort the lines in an efficient order
    lines = optimize_ordering(lines)

    print('done')

    # Preview what the drawing will look like
    preview_drawing(lines, speed=0, draw_movement=True, animation=False)

    # Convert to motor commands
    cmds = lines_to_motor_cmds(lines)

    # Connect to drawbot 
    print('Connecting to drawbot...', end='', flush=True)
    arduino = arduino_connect(port='/dev/cu.usbmodem14401')
    if not arduino:
        print('fail')
        return
    else:
        print('success')

    # Send motor commands
    cmd_counter = 0
    for motor1_steps, motor2_steps, draw in tqdm.tqdm(
        cmds, desc='Sending motor commands', unit='cmds'
    ):
        # Send the command
        arduino_write_cmd(arduino, motor1_steps, motor2_steps, draw)

        # Wait for confirmation
        cmd_num = arduino_read_int(arduino)
        #assert cmd_num == cmd_counter + 1, cmd_num

        cmd_counter += 1


def arduino_connect(port, baudrate=115200, timeout=5):
    arduino = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
    time.sleep(3)
    
    arduino.write(bytes('ready', 'utf-8'))
    time.sleep(0.05)
    
    res = arduino.readline().decode('utf-8').strip()
    return arduino if res == 'ack' else None


def arduino_write_cmd(arduino, motor1_pos, motor2_pos, draw=True):
    msg = ','.join(['1' if draw else '0', str(motor1_pos), str(motor2_pos), ''])
    
    arduino.write(bytes(msg, 'utf-8'))
    time.sleep(0.05)


def arduino_read_int(arduino):
    res = arduino.readline().decode('utf-8').strip()
    print(res)
    #return int(res)
    return res


def lines_to_motor_cmds(lines):
    def to_cmd(a, b, draw):
        dx = b.x - a.x
        dy = b.y - a.y

        assert -1.0 <= dx <= 1.0, (b.x, a.x)
        assert -1.0 <= dy <= 1.0, (b.y, a.y)

        x_steps = dx * min(WIDTH_STEPS, HEIGHT_STEPS)
        y_steps = dy * min(WIDTH_STEPS, HEIGHT_STEPS)

        motor1_steps = x_steps + y_steps
        motor2_steps = x_steps - y_steps

        return (motor1_steps, motor2_steps, draw)

    cmds = []
    prev = Point(0, 0)
    for i, line in tqdm.tqdm(
        enumerate(lines), desc='Converting lines to motor commands', unit='lines'
    ):
        if prev:
            cmds.append(to_cmd(prev, line[0], draw=False))

        for i in range(len(line) - 1):
            cmds.append(to_cmd(line[i], line[i + 1], draw=True))

        prev = line[-1]

    return cmds


if __name__ == '__main__':
    main()

    exit()
    
    # Some pretuned images and parameters as examples
    params = [
        dict(file_path='imgs/skull.png',
             hatch_pitch=4,
             levels=(24, 80, 128),
             blur_radius=15,
             invert=True),
        dict(file_path='imgs/lines.jpg',
             hatch_pitch=3,
             levels=(240, 240, 240),
             blur_radius=0),
        dict(file_path='imgs/lenna.png',
             hatch_pitch=2,
             levels=(102, 148, 200),
             blur_radius=8)
    ]

    # Converts an image to line drawing with diagonal hatching
    # Play with levels parameter and blurring to get right
    # Will error if contours too complicated
    mls = hatched.hatch(**params[1], save_svg=False, show_plot=False)

    mls = mls_normalize(mls) # put lines in unit square
    lines = list(mls_to_lines(mls)) # convert to simple list of list of points

    # Greedily sort the lines in an efficient order
    lines = optimize_ordering(lines)

    # Preview what the drawing will look like
    preview_drawing(lines, speed=0, draw_movement=False, animation=False)

    # Turn coordinates into proportional displacements and distances for robot
    # also includes whether drawing or not
    start_point, info = lines_to_robot_info(lines)
    
    # Here's an example of how you might use info:
    # distances are normalized for unit square
    # This info should be precomputed with hardcoded motorspeeds and scale
    WIDTH = 30 # cm
    HEIGHT = 30 # cm
    SCALE = min(WIDTH, HEIGHT)
    MOTORSPEED = 10 # cm/s

    # Assume these methods exist
    move_to_start = lambda start_point: None # easy if arm boots up at 0,0
    raise_pen = lambda: None
    lower_pen = lambda: None
    set_motor_x_speed_for_seconds = lambda speed, seconds: None
    set_motor_y_speed_for_seconds = lambda speed, seconds: None

    move_to_start(start_point)

    with open('output.txt','w') as f:
        for dx_norm, dy_norm, dist, draw in info:
            if draw:
                lower_pen()
            else:
                raise_pen()
                print('here\n')

            seconds = (dist * SCALE) / MOTORSPEED

            motor_x_speed = dx_norm * MOTORSPEED
            motor_y_speed = dy_norm * MOTORSPEED

            set_motor_x_speed_for_seconds(motor_x_speed, seconds)
            set_motor_y_speed_for_seconds(motor_y_speed, seconds)
            f.write(str(dx_norm)+ ", " + str(dy_norm)+ ", " + str(dist)+ ", " + str(draw)+ '\n')

