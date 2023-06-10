#
# _______  _______  ______  _______  __        
#|       ||   _   ||   __ \|     __||  |.-----.
#|   -  _||       ||      <|__     ||  ||  _  |
#|_______||___|___||___|__||_______||__||   __|
#                                       |__|   
# QARSlp Qtile + Arch Ricing System
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
from functions import *

# Theme
## Screens

def init_widgets_list():
    widgets_list = [
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        foreground=color[7],
        text=" QARSlp",
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.GroupBox(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        font=awesome_font,
        disable_drag=True,
        hide_unused=hide_unused_groups,
        borderwidth=0,
        active=color[6], #Program opened in that group
        inactive=color[8], # Empty Group
        rounded=False,
        highlight_method="block",
        this_current_screen_border=secondary_color[0],
        center_aligned = True,
        other_curren_screen_border=secondary_color[0],
        block_highlight_text_color=color[7],    
        urgent_border="fc0000",
        padding_y=10,
        padding_x=5,
        #visible_groups=['Escape','1','2','3','4']
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.Mpris2(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
        objname=None,
        foreground=color[7],
        width=widget_width,
        format='{xesam:artist}  {xesam:title}',
        stopped_text="Stop",
        paused_text='Paused',
        scroll=True,
        scroll_repeat=True,
        scroll_delay=0.1,
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.Prompt(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        prompt=prompt,
        foreground=color[7],
        cursor_color=color[7],
        visual_bell_color=[7],
        visual_bell_time=0.2,
      ),
      widget.Spacer(
        length=bar.STRETCH,
        background=transparent,
      ),
      widget.WindowName(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        foreground=color[7],
        width=widget_width,
        format='{name}',
        scroll=True,
        scroll_delay=2,
        scroll_repeat=True,
        scroll_step=1,
        padding=10,
      ),
      widget.Spacer(
        length=bar.STRETCH,
        background=transparent,
      ),
      widget.OpenWeather(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        app_key=w_appkey,
        cityid=w_cityid,
        weather_symbols={
          "Unknown": "",
          "01d": "",
          "01n": "🌕",
          "02d": "",
          "02n": "",
          "03d": "",
          "03n": "",
          "04d": "",
          "04n": "",
          "09d": "⛆",
          "09n": "⛆",
          "10d": "",
          "10n": "",
          "11d": "🌩",
          "11n": "🌩",
          "13d": "❄",
          "13n": "❄",
          "50d": "🌫",
          "50n": "🌫",
          },
          format='{icon} {temp}°{units_temperature}',
          foreground=color[7],
          metric=True,
          update_interval=600,
          padding=10,  
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ), 
      ## Network
        widget.TextBox(
          decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7],filled=True)],
          text=' ' + wifi_icon + ' ',
          foreground=color[7],
          mouse_callbacks={'Button1':lambda: qtile.spawn(home + "/.local/bin/wifi2")}
        ),
      widget.Wlan(
        decorations=[RectDecoration(colour=color[0],radius=0, filled=True)],
        interface=wifi,
        format='{percent:2.0%} ',
        disconnected_message='',
        foreground=color[3],
        mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
      ),
      widget.KeyboardLayout(
        decorations=[RectDecoration(colour=color[0], radius=[0,7,7,0],filled=True)],
        configured_keyboards=['us intl', 'latam'],
        foreground=color[7],
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.TextBox(
        decorations=[RectDecoration(colour=color[0], radius=[7,0,0,7], filled=True)],
        text="",
        foreground=color[7],
        mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol')}
      ),
      widget.ALSAWidget(
        decorations=[RectDecoration(colour=color[7], radius=[0,7,7,0], filled=True)],
        device='Master',
        bar_colour_high=color[0],
        bar_colour_loud=color[0],
        bar_colour_normal=color[0],
        bar_colour_mute=color[7],
        hide_interval=5,
        update_interval=0.1,
        bar_width=80,
        mode='bar',
        text_format=' ',
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.UPowerWidget(
          border_charge_colour=color[7],
          border_colour=color[6],
          border_critical_colour='#cc0000',
          fill_critical='#cc0000',
          fill_low='#FF5511',
          fill_normal=color[6],
          foreground=color[7],
          decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
          percentage_critical=0.2,
          percentage_low=0.4,
          text_charging=' ({percentage:.0f}%) {ttf} to ',
          text_discharging=' ({percentage:.0f}%) {tte} Left',
      ),
      widget.Spacer(
        length=5,
        background=transparent,
      ),
      widget.Clock(
        decorations=[RectDecoration(colour=color[0], radius=7, filled=True)],
        foreground=color[7],
        format="%A %H:%M",
        update_interval=1,
        mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
      ),
      
      ]
    return widgets_list

def screen1_widgets():
    widgets_screen1=init_widgets_list()
    return widgets_screen1


def init_screens_bottom():
    return[Screen(bottom=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=transparent,margin=bar_margin))]

def init_screens_top():
    return[Screen(top=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=transparent,margin=bar_margin))]

if bar_position == "top":
    screens=init_screens_top()
else:
  screens=init_screens_bottom()

widgets_list = init_widgets_list()
widgets_screen1 = screen1_widgets()