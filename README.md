# tkblock  
tkblock is a library to support easy placement of tkinter widgets.  
The method of placing widgets uses the old HTML/CSS idea of table layout.    


## Why we made it.
tkinter has three functions for placing widgets: place, grid, and pack.  
However, if you are not familiar with tkinter, it is difficult to distinguish between these three functions.  
At first, you may wonder which function to use for placement.  
I have often heard that after struggling with this problem, while checking the functions, they often fail to place them according to the UI diagram they have designed.  
Also, it was troublesome to install Windows Form and other software on my PC, and I could not use C# at my work place.
So, I decided to create a simple GUI application in python without worrying about OS or environment such as windows or linux.
As a result, I created a library that allows you to place widgets without having to be aware of the functions to be placed in tkinter.  


## Basic how to use
I will explain how to use the library.  


### Installing the library.

```bash
pip install tkblock
```
Install the library with.    

### Import the library and tkinter.

First, import the library.  
```python
import tkinter as tk
from tkinter import ttk
from tkblock.block_service import BlockService
```


### Creating the root window.

Create the root window using the imported library.  
When the root window is created, we specify the title, table width and height, and number of rows and columns.  
Next, place the widget by specifying its number of rows and columns when generating the widget.  

```python
root = BlockService.init("test", 10, 20, 600, 400)
```

The title of the application to be created by tkinter is "test".  
10 columns  
20 for the number of rows  
Width is 600  
Height is 400  

<img width="451" alt="readme_root" src="https://user-images.githubusercontent.com/78261582/223762154-a69ff349-c047-4793-a3aa-108bb21b03fe.png">

This figure shows the root window created by the above code.  

Note that you need to execute the written code to make root loop.  
```python
root.mainloop()
```

### Create a dedicated Frame.

Create a dedicated Frame on top of the root window for easy placement of the widget.  
```python
frame = BlockService.create_frame("main")
```

There are six arguments, but the only one that must be specified is the name of the Frame to be created.  
In this example, the frame name is "main".  
The optional arguments are as follows.  
+ col: The number of columns in the frame. If not specified, it is the number of columns in the destination window. In this case, 10.  
+ row: The number of rows in the frame. If not specified, it is the number of rows of the destination window. In this case, 20.  
+ width: The width of the frame. If not specified, it is the width of the destination window. In this case, 600  
+ height: The height of the frame. If not specified, it is the height of the destination window. In this case, it is 400  
+ root: The window where the frame will be placed. If not specified, the placement destination is the root window. In this case, the root window.  

By the way, to make it easier to see the table layout during development, a canvas is created internally to draw auxiliary lines.  
```python
BlockService.place_frame_widget()
```
You can draw an auxiliary line by executing the above code.  

``BlockService.place_frame_widget()``  
is explained in the next section.  

<img width="451" alt="readme_frame" src="https://user-images.githubusercontent.com/78261582/223762159-000cbd81-562e-4014-a8cf-8fa8a6d9d443.png">  

The Frame shown in this figure is the base for placing the widget.  

### Place the widget.

This time, we will place the simplest label.  

<img width="451" alt="readme_frame_add_layout" src="https://user-images.githubusercontent.com/78261582/223762161-b42a8cfc-11a5-4561-a883-4b641364d0b6.png">  

Suppose we want to place a label here.  
To do so, we specify the coordinates as follows.  
```python
BlockService.create_label(frame, 3, 6, 2, 4, text="how to use", anchor=tk.CENTER)
```
or 
```python
label = ttk.Label(frame, text="how to use", anchor=tk.CENTER)
label.layout = BlockService.layout(3, 6, 2, 4)
```

The above code is the same result as the two codes,  
It places a label in a frame with the text "how to use" in the center of the widget.  
The next argument specifies the value of layout.  
The values of layout are (column start position, column end position, row start position, row end position).  

Except for create_frame, the required arguments for all prepared create_xxx are: layout_frame, column_start_position, column_end_position, row_start_position, and row_end_position.  
All but a few of the optional arguments are passed as is to tk, ttk.  
In this case, text="how to use" is given to ttk.label.  
Please check docstring for what create_xxx series uses.  

The following is a list of functions to create widgets that we have prepared for you.  
```python
 'create_button', 'create_canvas', 'create_checkbutton', 
'create_combobox', 'create_entry', 'create_frame', 
'create_label', 'create_labelframe', 'create_listbox', 
'create_message', 'create_notebook', 'create_progressbar', 
'create_radiobutton', 'create_scale', 'create_scrollbar', 
'create_spinbox', 'create_text', 'create_toplevel', 'create_treeview'
```

This code is then added to the  

```python
BlockService.place_frame_widget()
```
Place it in front of the placed before the  
```python
BlockService.place_frame_widget()
```
place_frame_widget is a function that places all widgets owned by the root widdow.  
Therefore, it must be executed after all widgets have been created and layouts specified.  

<img width="451" alt="readme_frame_label" src="https://user-images.githubusercontent.com/78261582/223762164-25d5f489-3deb-42ea-87ca-ad290635214f.png">  


The label Widget is placed where intended, as shown in the above figure.  

### Basic Finished Code.  

This is the code created so far.  

```python
import tkinter as tk
from tkinter import ttk

from tkblock.block_service import BlockService

root = BlockService.init("test", 10, 20, 600, 400, is_debug=True)
frame = BlockService.create_frame("test")
BlockService.create_label(frame, text="how to use", 3, 6, 2, 4, anchor=tk.CENTER)
BlockService.place_frame_widget()
root.mainloop()
```

BlockService's in the tkblock library.  
+ init  
+ create_frame  
+ create_xxx  
+ place_frame_widget
You can easily use tkinter Widget just by using.  

<img width="897" alt="readme_widget" src="https://user-images.githubusercontent.com/78261582/225685418-ea328480-f051-4617-a459-d7af68ca8d5d.png">

In this figure, several Widget are placed in the above basic usage.  
Please try to create an application by placing various widgets.  

## About Layout padding settings

From here, I will explain a few details about the settings.  

First, let's talk about padding.  
This is similar to the function of padding, which is also found in html/css.  

<img width="448" alt="readme_layout1" src="https://user-images.githubusercontent.com/78261582/225678501-8c33f038-0874-4b52-80d1-74e80e0332e2.png">

As shown in the figure, the widget can be placed in the red area and the blue line gap can be set.  
You can use the margins by setting an optional argument to the layout method for that setting.  

```python
root = BlockService.init("test_pad", 3, 3, 600, 400)
frame = BlockService.create_frame("test_pad")
BlockService._create_label(frame, text="how to use pad", 1, 2, 1, 2, pad_up=0.3, pad_down=0.3, anchor=tk.CENTER, background="red")
```

Executing this code will result in the following.  

<img width="449" alt="readme_layout2" src="https://user-images.githubusercontent.com/78261582/225679256-11495187-e289-45b6-8d4c-b98c58c7f3ee.png">

pad_up sets the top margin.  
pad_down sets the bottom margin.
The value of 0.3 means that 30% of a block is used as the margin.  
There are also pad_left and pad_right.  
By setting these, fine adjustment is possible.  

<img width="898" alt="readme_layout3" src="https://user-images.githubusercontent.com/78261582/225679498-887d6429-d6eb-444f-9c26-80ff6068fca7.png">

This figure is created with Sample code.  
This is the code used when changing by 0.1, etc.  

## About Dedicated Frames

The previous code explained the Layout for placing the widget.  
This time, we will explain the special Frame provided by tkblock.  

The dedicated Frame is as described so far.  

```python
frame = BlockService.create_frame(name)
```

The Frame can be created with the following code.  
This code only allows a Frame to be placed on top of the root window.  
Since it is useful to be able to use Frame in many different places, an optional argument is provided.  
```
col: The number of columns that will make up the table in the newly created Frame.
row: The number of rows in the table of the newly created Frame.
width: The width of the table structure of the newly created Frame.
height: Table structure of the new Frame to be created.
root: Window or frame or top level where the frame will be placed.
```
the name of the window or frame or top level to which the frame will be placed.  
The root is the window or frame or top level where the frame will be placed.  
By specifying root, you can set the parent Frame, etc.  
The items other than ``root'' are the table structure for creating a new Frame, and if not specified, it inherits the parent's settings.  
Also, as with widgets, the layout method can be used to change the location of the Frame.  
As a test, let's place a dedicated Frame on top of the root window and a dedicated Frame on top of it.  

<img width="447" alt="readme_frame1" src="https://user-images.githubusercontent.com/78261582/225680361-4f1eb045-6107-41cb-81fe-00e804ce47d2.png">

```python
root = BlockService.init("test_frame", 10, 10, 600, 400)
frame1 = BlockService.create_frame("test_frame1", col=5, row=5)
frame1.layout = BlockService.layout(1, 9, 1, 9)
frame2 = BlockService.create_frame("test_frame2", col=3, row=3, root=frame1)
frame2.layout = BlockService.layout(1, 3, 2, 4)
BlockService.place_frame_widget()
root.mainloop()
```

In this code, test_frame1 is placed at coordinates (1,1)(9,9) of root, and  
test_frame2 is placed at coordinates (1,2)(3,4) of test_frame1.  
The table structure of each frame is also changed.  
In this way, a dedicated Frame can be placed on top of a dedicated Frame, which is useful when you want to group Widgets together.  

<img width="895" alt="readme_frame2" src="https://user-images.githubusercontent.com/78261582/225680783-c3a0a89c-62d6-4a95-bf3b-f617b3b0dfbe.png">

In the sample, a dedicated frame is placed on top of a regular frame or on the toplevel.   

## About Scrollbar Settings

So far, we have discussed how to place a Widget, how to use  
Frame to place the Widget and how to make detailed adjustments to place the Widget.  
The application has a size, and the root window and Frame had height and width settings.  
However, tkinter provides scrollbars when the specified size does not fit.  
Scrollbars are used in conjunction with widgets such as canvas and listbox.  
Therefore, basically, widgets and scrollbars are placed side by side.  
The scrollbars can also be placed where you want them by using the layout method, but in this case, the scrollbars are placed on the right side of the widget.  
In this article, we will explain how to use this method to automatically set scrollbars on the right and bottom sides of a widget.  

To use it, simply set the scrollbar on the widget you wish to link to the scrollbar.

```python
scrollbar_listbox = tk.Listbox(frame)
scrollbar_listbox.scrollbar = BlockService.scrollbar(frame, y_enable=True)
```

In this case, Scrollbar is set to the attribute named scrollbar in the listbox.  
By setting it to the y-axis, you can set up a vertical scrollbar.  
You can also set scrollbars on the x-axis to set left and right scrollbars.  

The size of the scrollbar is fixed at 17px, and 17px is shaved off from the size of the widget to place it.  
Therefore, when using scrollbars, the Widget will be slightly smaller.  
You can change the size of the scrollbars by setting the optional argument "size".  

<img width="448" alt="readme_scrollbar1" src="https://user-images.githubusercontent.com/78261582/225681324-18c8a73a-047b-4704-925b-dfb66a44882b.png">

In the above figure, 30px vertical and horizontal scrollbars are placed.
The code for this is shown below.

```python
root = BlockService.init("test_scrollbar", 5, 5, 600, 400, is_debug=True)
frame = BlockService.create_frame("test_scrollbar")
listbox_list = tuple([str(x) for x in range(0, 100)] + ["aabfsdgadfsgasdfkj;adsfadsj;kjfeijof"])
_, listbox_var = tk.Listbox(frame, 1, 2, 1, 4, init_value=listbox_list)
listbox.scrollbar = BlockService.scrollbar(frame, x_enable=True, y_enable=True, size=30)
BlockService.place_frame_widget()
root.mainloop()
```

The basic usage of the scrollbar is the same. If you want the scrollbar to be placed automatically, you can place it by linking the scrollbar to the widget.  
If you wish to manually place it anywhere you wish, simply specify the layout as you would for a normal widget.  

## How to use the Menu bar
Omitted since it is the same as the usage of tkinter. 

## bonus. wait_processe.
The "BlockService.wait_processe" function is used to draw the waiting screen during processing.  
An example is used in topleve_split_file.py under Sample.  
This is a decorator function to decorate the currently executing function.  
For example, when a function assigned to a button widget is executed, it will output a waiting dialog.   

<img width="218" alt="wait_process1" src="https://github.com/kuri-pome/tkblock/assets/78261582/03c4680c-4de0-4047-89f6-75cc732ec2f9">

To use it, simply set the target frame as an argument and decorate it.  
```python
@wait_processe()
def _split_file(
```


# Summary.  
If you are going to make a full-fledged app, I would prefer not to use this.  
I think a small app would be useful.  
(I'm just concerned that I haven't done much testing...)  

By the way, the code is in the Samples folder on github, so you might want to take a look at it.  

Well, thank you for viewing this far.  