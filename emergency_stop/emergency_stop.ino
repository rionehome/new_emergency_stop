/* Arduino uno */

const int r = 2;

int res;

void setup(){
  pinMode(r, INPUT_PULLUP);
 
  Serial.begin(9600);
}
 
 
void loop(){
  res = digitalRead(r);
  
  Serial.println(res);
 
  delay(100);
}
