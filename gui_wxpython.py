import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        panel = wx.Panel(self)
        
        # Load an image and create a bitmap
        mic_bitmap = wx.Bitmap("tool.png", wx.BITMAP_TYPE_PNG)

        # Create a button with the image and text
        mic_button = wx.Button(panel, label="🎤", size=(120, 50))
        mic_button.SetBackgroundColour(wx.Colour(255, 0, 0))  # Red background
        mic_button.SetForegroundColour(wx.Colour(255, 255, 255))  # White text

        # Set the image as the bitmap for the button
        mic_button.SetBitmap(mic_bitmap)

        # Create a horizontal box sizer to arrange the button
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(mic_button, flag=wx.LEFT | wx.ALIGN_CENTER_VERTICAL, border=10)

        panel.SetSizer(hbox)

    def on_button_click(self, event):
        wx.MessageBox("You clicked the microphone button!", "Info", wx.OK | wx.ICON_INFORMATION)

def main():
    app = wx.App(False)
    frame = MyFrame(None, title="wxPython Button with Image", size=(300, 200))
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
