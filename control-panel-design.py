/* 
This section involves python script for the design of a desktop control panel using wxPython library. This is a subpart of a WCR for industrial 
inspection project in TLC under the guidance of Dr. S. R. pandian and is being done by  Mr. Amit Sharma, M.Des EDS 2016 batch, roll no. 
eds16m007.   
*/

import wx
import wx.xrc
import cv, cv2
import numpy as np



class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"WALLROBO (IIITDM KANCHEEPURAM)", pos = wx.DefaultPosition, size = wx.Size( 1200,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"START STREAMING", wx.DefaultPosition, wx.DefaultSize, 0|wx.FULL_REPAINT_ON_RESIZE )
		bSizer18.Add( self.m_button6, 0, wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, u"STOP STREAMING", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_button8 = wx.Button( self, wx.ID_ANY, u"START PROCESS", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button8, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self, wx.ID_ANY, u"STOP PROCESS", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"MOVE FRONT", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button10, 0, wx.ALL, 5 )
		
		self.m_button11 = wx.Button( self, wx.ID_ANY, u"MOVE DOWN", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button11, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"TURN LEFT", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_button12, 0, wx.ALL, 5 )
		
		self.m_button13 = wx.Button( self, wx.ID_ANY, u"TURN RIGHT", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_button13, 0, wx.ALL, 5 )
		
		
		bSizer19.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetMinSize( wx.Size( 540,420 ) )
		
		bSizer2.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3.SetMinSize( wx.Size( 10,-1 ) ) 
		
		bSizer3.AddSpacer( ( 10, 0), 0, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"TEMPERATURE                          :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer5.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"HUMIDITY                                 :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer7.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"CURRENT                                  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer8.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"VOLTAGE                                  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer9.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"POWER                                     :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer10.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"SPEED                                       :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer11.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_textCtrl6, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"CLEANER                                :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer12.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_textCtrl8, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"CLEANER                                :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer13.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_textCtrl9, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"THROTTLE ADJUSTMENT   :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer14.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_textCtrl10, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer14.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_slider1 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer14.Add( self.m_slider1, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"100", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer14.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"CLEANER ARM UP       ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"CLEANER ARM DOWN", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button4 = wx.Button( self, wx.ID_ANY, u"START CLEANING", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"STOP CLEANING   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button5, 0, wx.ALL, 5 )
		
		
		bSizer15.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

class ShowCapture(wx.Panel):
    def __init__(self, parent, capture, fps=15):
        wx.Panel.__init__(self, parent)

        self.capture = capture
        ret, frame = self.capture.read()

        height, width = frame.shape[:2]
        parent.SetSize((width, height))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.bmp = wx.BitmapFromBuffer(width, height, frame)

        self.timer = wx.Timer(self)
        self.timer.Start(1000./fps)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.NextFrame)


    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def NextFrame(self, event):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.bmp.CopyFromBuffer(frame)
            self.Refresh()


capture = cv2.VideoCapture(0)
capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 320)
capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 240)



if __name__=="__main__":
    app = wx.App()
    fm = MyFrame1(None)
    
    fm.Show()
    cap = ShowCapture(fm.m_panel2, capture)
    app.MainLoop()
