# new_emergency_stop

緊急停止ボタンで、ROSの動きを止めるやつです。  
launchファイルで一緒に起動させる組み込み型と、独立してROSシステムを停止させる独立型を用意しました。  
組み込み型は、launchファイル内のすべてのノードを停止させるのに対し、  
独立型は、実行中のすべてのROSプロセスを停止させます。  

## 使い方
### 組み込み型
白い配線を、ArduinoのGNDに、  
黒い配線を、Arduinoの2番につけます。  
詳しくは、ソースコードをご覧ください。  

ボタンが押されたら停止したいlaunchファイル内に、  
```
<node pkg="new_emergency_stop" name="emergency_stop_build_in_type" type="build_in_type.py" required="true" output="screen" />
```
を追加します。  
Arduinoに書き込み、launchファイルを起動させます。  
ボタンを押すと、launchファイル内のすべてのノードが止まります。  


### 独立型
白い配線を、ArduinoのGNDに、  
黒い配線を、Arduinoの2番につけます。  
詳しくは、ソースコードをご覧ください。  

Arduinoに書き込み、このファイルを実行します。  
ボタンを押すと、実行中のすべてのROSプロセスが止まります。
