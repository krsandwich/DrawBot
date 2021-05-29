# Drawbot

This is a parts list and assembly guide for the Lab64 drawbot, a small desktop robot that draws cool pictures for you. 

## Background 
The goal of this project is to build a desktop bot which can hold a pen and use it to draw images on a sheet of paper. Achieving this requires two main components -- the ability to move precisely in the XY plane over the paper, and the ability to lift a pen on and off of the paper. 

- **XY motion**
The XY motion is driven by two Nema-17 stepper motors, one mounted to each end of the x axis. [Here](https://www.youtube.com/watch?v=_nzxGOKhHSY ) is a visualization of how driving the stepper motors in sync and against each other allows the carriage to move in 3D.

- **Pen lifting**
The lifting of the pen is driven by a tiny SG90 servo. The pen will drop down by gravity when the servo is not blocking it. To lift the pen up, the servo rotates, lifting the pen-holder up and moving the pen off the paper. 

## Parts list

### Tools & Bolts
|  Item No  |  Qty / kit |  Description |  Link |
| :-------- | :----------------- | :-------------- | :-------------- |
| 1 | 1 | Metric m5 allen key | [Amazon](https://www.amazon.com/Eklind-14610-Long-Hex-L-Key/dp/B000GAOAFK/)  |
| 2 | 1 | M5 bolt + nut set | [Amazon](https://www.amazon.com/DYWISHKEY-Pieces-Stainless-Steel-Button/dp/B07WZHN2XS/) |
| 3 | 12 | M5 t-nuts | [Amazon](https://www.amazon.com/100Pcs-T-Nuts-Carbon-Nickel-Plated-Sliding/) |

### Hardware
|  Item No  |  Qty / kit |  Description |  Link |
| :-------- | :----------------- | :------------- | :-------------- |
| 4 | 1 | Openbuilds 20x40x500 v-slot | [Openbuilds](https://openbuildspartstore.com/v-slot-20x40-linear-rail/) |
| 5 | 1 | Openbuilds 20x20x250 v-slot | [Openbuilds](https://openbuildspartstore.com/v-slot-20x20-linear-rail/) |
| 6 | 6 | V-slot wheels | [Amazon](https://www.amazon.com/AFUNTA-Plastic-Bearings-Printer-Compatible/dp/B07KPWJ3ZC/) |
| 7 | 5 | Bearings **could be 3d printable | [Amazon](https://www.amazon.com/gp/product/B07JMRR7CC/) |
| 8 | 1 | GT2 belt | [Amazon](https://www.amazon.com/Upgrade-Non-Slip-Abrasion-Resistance-Printers/dp/B08NVL55HC/) |


### Electronics
|  Item No  |  Qty / kit |  Description |  Link |
| :-------- | :----------------- | :-------------- | :-------------- |
| 9 | 1 | Elegoo uno board | [Amazon](https://www.amazon.com/ELEGOO-Board-ATmega328P-ATMEGA16U2-Compliant/dp/B01EWOE0UU/) |
| 10 | 2 | Nema17 stepper motor | [Amazon](https://www.amazon.com/RTELLIGENT-Stepper-Bipolar-42x42x38mm-42A02C-XH2-54/dp/B0817TGDQM/?th=1) |
| 11 | 2 | A4988 stepper driver | [Amazon](https://www.amazon.com/ARCELI-Compatible-Stepper-StepStick-Controller/dp/B07MXXL2KW) |
| 12 | 1 | Towerpro micro servo | [Amazon](https://www.amazon.com/Smraza-Helicopter-Airplane-Control-Arduino/dp/B07L2SF3R4/ ) |
| 13 | 1 | Jumper wire | [Amazon](https://www.amazon.com/EDGELEC-Breadboard-Optional-Assorted-Multicolored/dp/B07GD431C1/) |
| 14 | 1 | Breadboard | [Amazon](https://www.amazon.com/Breadborad-Solderless-Breadboards-Distribution-Connecting/dp/B082VYXDF1/) |
| 15 | 2 | 9V battery | [Amazon](https://www.amazon.com/Energizer-Alkaline-Volt-Batteries-Count/dp/B01AVK3NMU/) |
| 16 | 2 | Battery hats | [Amazon](https://www.amazon.com/Battery-Connector-Leather-Housing-Connection/dp/B06X8YZJ64/) |

### 3D Prints
|  Item No  |  Qty / kit |  Description | 
| :-------- | :----------------- | :-------------- | 
| 17 | 2 | Stepper mount | 
| 18 | 2 | GT2 pulley for stepper | 
| 19 | 1 | Lower cart |
| 20 | 1 | Upper cart | 
| 21 | 4 | Cart spacers |
| 22 | 4 | Pulley spacers |
| 23 | 1 | Back pulley |
| 24 | 1 | Servo mount | 
| 25 | 1 | Pen mount |
| 26 | 1 | Belt clamp | 



## Mechanical Assembly

If you're coming here from the recent workshop, these instructions will be in a different order than you may remember. I recommend following these instructions from the start, and you may find that you've already done some steps as you go. 

These instructions may be difficult to follow in places -- I don't have enough photos, and don't have enough bolts to recreate the bot to take the photos. If you have trouble, we'll be having a second catcup-up mechanical session while people with the mechanics completed work on the electronics (electronics are far easier to complete on your own)

### Bolts
Your kit has the following bolts:
|  Item  |  Qty / kit |  Description | 
| :-------- | :----------------- | :-------------- | 
| M5 T-Nuts | 8 + 5 extra | Silvery oblong nuts with a hole in the middle | 
| M5 hex nuts | 7 + 5 extra | Hexagonal nuts with a hole in the middle | 
| M5x10 bolts | 8 | Shortest size |
| M5x12 bolts | 6 | Second-shortest (very hard to differentiate from M5x10s, be careful!) | 
| M5x16 bolts | 8 | Second-longest |
| M5x20 bolts | 6 OR 12 | Longest size |
| M5 allen key | 1 | Allen key used to screw in bolts |

Begin by sorting your bolts. It's okay if you have one more or less of each type.

### Stepper motor
Begin with the 2 Nema 17 stepper motors, 2 GT2 pulleys, and 2 stepper mounts (pictured below). To push the pulley onto the motor, look closely at the stepper motor axle and notice that they are not perfectly round, they have one flat edge. Line up that flat edge with the flat edge on the 3d printed pulley, flip the whole thing upside down, and push down hard against a flat object until the pulley is flush with the axle. Then, take the stepper mount. Orient the long side in the same direction as the stepper motor wires, and push until it snaps into place. It should hold without any screws. 

<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/2.png" width="500">
<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/3.png" width="500">

### Main carriage
Select 6 M5x20s (20 mm long 5mm bolts), 6 M5 hex nuts, the black wheels, and the two round 3d printed carts. There are hexagonal holes on the insides of the carts, opposite the square lumps -- press the nuts in, they should snap into place. Flip the cart over and attach the wheels to the lumps with the M5x20s. You should leave the bolts just slightly loose; make sure that all wheels can spin freely.

<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/4.jpg" width="500">
<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/5.jpg" width="500">

One of the carts has four holes in the centre. The one with the holes is the lower cart, and the other is the upper cart. Take the lower cart, and insert four M5x12s through the center 4 holes, passing from the lumpy side to the inside (bolt head stays on the lumpy side). These will be used to hold pulleys. Slide the tiny spacers onto the M5x12s from the inside of the cart, with the slightly wider side down presing against it.  

<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/7.jpg" width="500">


Next, you will put in the spacers using four M5x16 bolts, as pictured. Once this is done, place the metal pulleys onto the middle M5x12s. You can then pick up the top cart and place it onto the bottom one. Tighten the M5x16s to connect. 

<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/10.jpg" width="500">
<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/11.png" width="500">


### Attaching to metal
You will use small metal t-nuts in order to attach to the metal extrusion. The t-nuts will fit into the slots in the metal, and you will be able to put a M5x10 bolt through and tighten it to create a strong attachment. Begin with one of the stepper motors, and put two M5x10s through the holes. Then, thread the t-nuts ever-so-slightly on as pictured. Slide the larger piece of aluminum extrusion into the t-nuts, and tighten them down. They should create a firm attachment. If they do not, loosen them and try again -- it may take a few tries and some practice. When you're done, you will be able to shake pieces around and have it hold solidly without slipping at all. 

Then, you can roll the carriage onto the extrusion. Push the smaller piece of extrusion onto the upper cart. After the carriage is rolled onto the lower extrusion, you can attach the second stepper motor. 

<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/12.png" width="500">
<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/13.png" width="500">

### Attaching back pulley
Attach the last metal pulley to the U-shaped back pulley piece, with a M5x16 bolt passing loosely through the print from below up into the pulley. Then use the same strategy with the t-nuts and two M5x10s to attach the U-shaped back pulley piece to the small piece of metal extrusion. There are four potential holes you can use; I recommend just starting with two bolts diagonally across from each other. 
<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/thumbnail_IMG_4842.jpeg" width="500">

### Pen mount
Begin by attaching the servo (in blue, in the photo) to the pen mount (in yellow). You can use the tiny pointy bolts that come with the servo bag, and use your fingers to tighten it as much as you can. Then affix the pen mount (in yellow) to the metal, using 2M5x10s, 2 t-nuts and the same procedure you just used for the back pulley. Next, you will run the belt, before completing the pen mount. 

<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/final_pen_mount.png" width="500">

### Running the belt
Running the belt is the trickiest part of the assembly. The belt must run around all of the pulleys in a plus sign, to transmit the motion of the steppers into the carriage. Begin by poking one end of the belt into the stepper mount. There are two parallel slots for the belt, slide one end through with the orientation shown in the diagram. Then cut a length of belt, and slide the opposite end into and out of the carriage in the pattern shown. I recommend getting chopsticks, tweezers, or a fork to grab the belt and move it aorund. If this does not work for you, undo the spacer bolts keeping the upper and lower cart together, loop the belt, and reassemble the carriage. Once you're done, pass it through the second slot in the stepper mount, and trim any extra. Tighten down the spiny piece using the center bolt to clamp the belt in place. 

If you hold the pulleys and twist them, the carriage should move. Moving the motors in the same direction will move the carriage left and right, and moving the motors in opposite directions will move the carriage back and forth. 

![Belt diagram](https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/belt.png)

### Attaching the pen
Attach the pen swivel (in light blue in the image in the Pen Mount section) to the pen mount, using 2 M5x12s. The swivel should be able to rotate up and down when the servo turns. Once you're sure that's in place, take any pencil. Clamp it to the pen swivel using 2 M5x16s, using the pen clamp (orange in the image). 

## Electronics

All electronics will be conected using the breadboard and jumper wires. This is a quick and easy way to prototype mechatronic systems. Full electronics photo TBD. 

### Stepper motors
Breadboards are connected horizontally. Gently push the red A4988 onto a breadboard, with each row of pins on a different half of the board. Make sure that the orientation matches the diagram, and link the wires as pictured. Repeat a second time for the second A4988 and second stepper motor, making sure to connect to pins 3&4 for the first and then 12&13 for the second on the elegoo. 
<img src="https://code.stanford.edu/lab64/Projects/-/raw/master/Draw_Bot/Photos%20of%20project/A4988-Wiring-Diagram.png" width="500">


### Servo
TBD.



## Code
The Elegoo board can be run directly from the Arduino software. Download the Arduino IDE here: https://www.arduino.cc/en/software

Test that your stepper motors are working by downloading the stepper test code from the "Starter Code" file. It should make your steppers run in a square, wait, and then do it again in an infinite loop. If your stepper motors are screaming and not rotating, please let us know and we can debug.

Now that you have that running, we will upload the real code. Please do the following: <br/>


`git clone https://github.com/krsandwich/DrawBot.git` <br/>
`cd DrawBot/drawbot_code` <br/>
`python3 -m venv .env` <br/>
`source .env/bin/activate` <br/>
`python3 -m pip install -r requirements.txt`<br/><br/>
Now, open drawbot_arduino and run the sketch making sure to specify the correct port for your arduino. Copy down the port name and put it in line 73 of drawbot.py. Now run the following command:<br/><br/>
`
python3 drawbot.py
`<br/><br/>
You will see a hello world graphic pop up! The black lines represent lines that will be drawn and red lines represent movement. Make sure your motors are connected to power (you should hear an annoying buzz) and that the arduino script is running. Now you can close the Hello World window and the drawbot should start drawing! You'll notice that the current code does not use the servo to lift the pencil during the red line areas. We will update that within the next week OR you can accept the challenge and write the code yourself. If you get it working, send the code to us for a HUGE prize :). 




