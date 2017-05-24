#define DE_RE 3
#define id 0x05
#define func 0x03
#define addr1 0x0B
#define addr2 0xDC
byte  buf[8] = {0x07, 0x03, 0x0B, 0xD7, 0x00, 0x02, 0x77, 0x8D};
byte bufO[80];
void transmit()
{
  digitalWrite(DE_RE, HIGH);
  Serial.println("Transmitting");
}

void receiver()
{
  digitalWrite(DE_RE, LOW);
  Serial.println("Receiving");
}

void setup() {
  // put your setup code here, to run once:

 // pinMode(DE_RE, OUTPUT);
  Serial.begin(115200);
  Serial2.begin(9600, SERIAL_8N1);

  for(int i = 1; i<=20; i++)
    bufO[i] = 0x00;
}

void loop() {
  // put your main code here, to run repeatedly:
  int result = 0x0;
 // transmit();//05030BB70002778D
 
  int buff;
  Serial2.write(buf, 8);
  //delay(100);
  //receiver();
  delay(1000);
  if(Serial2.available()>0){
  
  buff = Serial2.readBytes(bufO, 20);
//  sprintf(&buff, "the current value is %d", 16);
  delay(100);
  for(int i=1; i<=20; i++)
  {
    Serial.print(bufO[i], HEX);
    Serial.print(",");
  }}
  //Serial.println(buff);
  //delay(3000);
}
