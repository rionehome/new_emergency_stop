# new_emergency_stop

緊急停止ボタンで、ROSの動きを止めるやつです。

## 使い方
白い配線を、ArduinoのGNDに、
黒い配線を、Arduinoの2番につけます。
詳しくは、ソースコードをご覧ください。

ボタンが押されたら停止したいlaunchファイル内に、
'''
<node pkg="new_emergency_stop" name="emergency_stop" type="emergency_stop.py" required="true" output="screen" />
'''
を追加します。

Arduinoに書き込み、launchファイルを起動させます。

ボタンを押すと、launchファイル内のすべてのノードが止まります。
