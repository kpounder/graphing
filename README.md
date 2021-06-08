### Better Seaborn Plots

We provide a function to overwrite some Seaborn plot defaults in order to produce better data visualizations. The inspiration for the design choices is Storytelling with Data: A Data Visualization Guide for Business Professionals by Cole Nussbaumer Knaflic. (If you have not read/seen that book, check it [out](https://www.amazon.com/gp/product/1119002257/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=storytellingwithdata-20&creative=9325&linkCode=as2&creativeASIN=1119002257&linkId=c9a5d9689e0665c8098acb1bd01b51e1)!) 

Here are some example visualizations: 

**Line Plot** 
> Do you need a grid? Let's remove unnecessary elements to focus the viewer's eyes.

![Line Plot](https://github.com/kpounder/graphing/blob/327c8dc73af6d01c6e3e4e24cda2291e7a4e3a3a/examples/line.png?raw=true)

**Sub Plots with Shared Horizontal Axis**
> This is an alternative to dual axes, which often require more to understand and communicate incorrect information (e.g., do the "intersecting lines" really intersect?).

> Removing unnecessary elements once again -- no need for two sets of x-tick labels or x-axis labels if they're the same. Arrange the visual to take advantage of that. 

![Sub Plots](https://github.com/kpounder/graphing/blob/327c8dc73af6d01c6e3e4e24cda2291e7a4e3a3a/examples/subplots.png?raw=true)

**Bar Plot**
> Use color wisely: What do you want the reader to see right away? 

![Bar Plot](https://github.com/kpounder/graphing/blob/773da43e3433cbb426f95430c77ba1a3ddfbafdf/examples/bar.png?raw=true)

This repo contains the following files:

* custom_seaborn.py:
    * Contains the main function, customize_axis, which customizes a Matplotlib Axis object

* examples.py: 
    * A few data viz examples

* preferences.yaml
    * Contains the desired font sizes, fonts, colors, etc.

* requirements.txt
    * Required libraries 
