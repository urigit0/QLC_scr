
a = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Workspace>
<Workspace xmlns="http://www.qlcplus.org/Workspace" CurrentWindow="FunctionManager">
 <Creator>
  <Name>Q Light Controller Plus</Name>
  <Version>4.12.4</Version>
  <Author>User</Author>
 </Creator>
 <Engine>
  <InputOutputMap>
   <Universe Name="Universe 1" ID="0">
    <Input Plugin="ArtNet" Line="4"/>
    <Output Plugin="ArtNet" Line="4"/>
   </Universe>
   <Universe Name="Universe 2" ID="1"/>
   <Universe Name="Universe 3" ID="2"/>
   <Universe Name="Universe 4" ID="3"/>
  </InputOutputMap>
  <Fixture>
   <Manufacturer>Generic</Manufacturer>
   <Model>Generic RGBW</Model>
   <Mode>RGBW</Mode>
   <ID>0</ID>
   <Name>Generic RGBW #1</Name>
   <Universe>0</Universe>
   <Address>0</Address>
   <Channels>4</Channels>
  </Fixture>
  <Fixture>
   <Manufacturer>Generic</Manufacturer>
   <Model>Generic RGBW</Model>
   <Mode>RGBW</Mode>
   <ID>1</ID>
   <Name>Generic RGBW #2</Name>
   <Universe>0</Universe>
   <Address>4</Address>
   <Channels>4</Channels>
  </Fixture>
  <Fixture>
   <Manufacturer>Generic</Manufacturer>
   <Model>Generic RGBW</Model>
   <Mode>RGBW</Mode>
   <ID>2</ID>
   <Name>Generic RGBW #3</Name>
   <Universe>0</Universe>
   <Address>8</Address>
   <Channels>4</Channels>
  </Fixture>
  <Fixture>
   <Manufacturer>Generic</Manufacturer>
   <Model>Generic RGBW</Model>
   <Mode>RGBW</Mode>
   <ID>3</ID>
   <Name>Generic RGBW #4</Name>
   <Universe>0</Universe>
   <Address>12</Address>
   <Channels>4</Channels>
  </Fixture>
  <Fixture>
   <Manufacturer>Generic</Manufacturer>
   <Model>Generic RGBW</Model>
   <Mode>RGBW</Mode>
   <ID>4</ID>
   <Name>Generic RGBW #5</Name>
   <Universe>0</Universe>
   <Address>16</Address>
   <Channels>4</Channels>
  </Fixture>
  <Fixture>
   <Manufacturer>Generic</Manufacturer>
   <Model>Generic RGBW</Model>
   <Mode>RGBW</Mode>
   <ID>5</ID>
   <Name>Generic RGBW #6</Name>
   <Universe>0</Universe>
   <Address>20</Address>
   <Channels>4</Channels>
  </Fixture>
  <Function ID="0" Type="Scene" Name="New Scene" Hidden="True">
   <Speed FadeIn="0" FadeOut="0" Duration="0"/>
   <FixtureVal ID="0">3,0</FixtureVal>
   <FixtureVal ID="1">3,0</FixtureVal>
   <FixtureVal ID="2">3,0</FixtureVal>
   <FixtureVal ID="3">3,0</FixtureVal>
   <FixtureVal ID="4">3,0</FixtureVal>
   <FixtureVal ID="5">3,0</FixtureVal>
  </Function>
  <Function ID="1" Type="Sequence" Name="New Sequence 1" BoundScene="0">
   <Speed FadeIn="0" FadeOut="0" Duration="0"/>
   <Direction>Forward</Direction>
   <RunOrder>Loop</RunOrder>
   <SpeedModes FadeIn="Default" FadeOut="Default" Duration="Common"/>
   <Step Number="0" FadeIn="0" Hold="0" FadeOut="0" Values="6">1:3,255:3:3,255</Step>
   <Step Number="1" FadeIn="0" Hold="0" FadeOut="0" Values="6">2:3,255:4:3,255</Step>
   <Step Number="2" FadeIn="0" Hold="0" FadeOut="0" Values="6">0:3,255:2:3,255</Step>
   <Step Number="3" FadeIn="0" Hold="0" FadeOut="0" Values="6">3:3,255:5:3,255</Step>
  </Function>
  <Function ID="2" Type="Scene" Name="New Scene" Hidden="True">
   <Speed FadeIn="0" FadeOut="0" Duration="0"/>
   <FixtureVal ID="0">3,0</FixtureVal>
   <FixtureVal ID="1">3,0</FixtureVal>
   <FixtureVal ID="2">3,0</FixtureVal>
   <FixtureVal ID="3">3,0</FixtureVal>
   <FixtureVal ID="4">3,0</FixtureVal>
   <FixtureVal ID="5">3,0</FixtureVal>
  </Function>
  <Function ID="3" Type="Sequence" Name="New Sequence 3" BoundScene="2">
   <Speed FadeIn="0" FadeOut="0" Duration="0"/>
   <Direction>Forward</Direction>
   <RunOrder>Loop</RunOrder>
   <SpeedModes FadeIn="Default" FadeOut="Default" Duration="Common"/>
   <Step Number="0" FadeIn="0" Hold="0" FadeOut="0" Values="6">0:3,255</Step>
   <Step Number="1" FadeIn="0" Hold="0" FadeOut="0" Values="6">1:3,255</Step>
   <Step Number="2" FadeIn="0" Hold="0" FadeOut="0" Values="6">2:3,255</Step>
  </Function>
  <Function ID="4" Type="Scene" Name="New Scene" Hidden="True">
   <Speed FadeIn="0" FadeOut="0" Duration="0"/>
   <FixtureVal ID="0">0,0,1,0,2,0,3,0</FixtureVal>
   <FixtureVal ID="1">0,0,1,0,2,0,3,0</FixtureVal>
   <FixtureVal ID="2">0,0,1,0,2,0,3,0</FixtureVal>
   <FixtureVal ID="3">0,0,1,0,2,0,3,0</FixtureVal>
   <FixtureVal ID="4">0,0,1,0,2,0,3,0</FixtureVal>
   <FixtureVal ID="5">0,0,1,0,2,0,3,0</FixtureVal>
  </Function>
  <Function ID="5" Type="Sequence" Name="New Sequence 5" BoundScene="4">
   <Speed FadeIn="0" FadeOut="0" Duration="0"/>
   <Direction>Forward</Direction>
   <RunOrder>Loop</RunOrder>
   <SpeedModes FadeIn="Default" FadeOut="Default" Duration="Common"/>
   <Step Number="0" FadeIn="0" Hold="0" FadeOut="0" Values="24">0:2,255,3,255</Step>
   <Step Number="1" FadeIn="0" Hold="0" FadeOut="0" Values="24">0:0,255,1,255</Step>
  </Function>
 </Engine>
 <VirtualConsole>
  <Frame Caption="">
   <Appearance>
    <FrameStyle>None</FrameStyle>
    <ForegroundColor>Default</ForegroundColor>
    <BackgroundColor>Default</BackgroundColor>
    <BackgroundImage>None</BackgroundImage>
    <Font>Default</Font>
   </Appearance>
  </Frame>
  <Properties>
   <Size Width="1920" Height="1080"/>
   <GrandMaster ChannelMode="Intensity" ValueMode="Reduce" SliderMode="Normal"/>
  </Properties>
 </VirtualConsole>
 <SimpleDesk>
  <Engine/>
 </SimpleDesk>
</Workspace>
"""






index = 0
while True:
    index = a.find('New Sequence 1', index, -1)     # находим Sequence....
    if index < 0:
        break
    index = a.find('Step', index, -1) # находим начало
    # print(a[index:-1])
    index_2 = a.find('</Function>', index, -1) # находим конец данных секвенции
    step = 0
    for step in range(1):
        index = a.find('Values="', index, index_2)  # находим начало
        index = a.find('">', index, index_2)  # находим начало
        nim_fixt = 20


    print(a[index:index_2])


