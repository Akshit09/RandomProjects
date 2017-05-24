int i=0; 
int j=0;
void setup()
{
  for(i = 2; i<=11 ;i++)
  pinMode(i, OUTPUT);
  digitalWrite(i, LOW);
}
void switchoff()
{
  for (i=2; i<=11; i++)
  digitalWrite(i, LOW);

}
void LowPinsHigh()
{
  for(i=7; i<=11; i++)
  digitalWrite(i, HIGH);

}
void HighPinsLow()
{
  for(i=2; i<=6; i++)
  digitalWrite(i, LOW);
}
void LowPinsLow()
{
  for(i=7; i<=11; i++)
  digitalWrite(i, LOW);

}
void loop()
{
  for(j=0; j<=1000; j++)
{
  digitalWrite(2, HIGH);
  LowPinsLow();
  delay(1);
  LowPinsHigh();
  HighPinsLow();
  digitalWrite(3, HIGH);
  digitalWrite(7, LOW);
  digitalWrite(11, LOW);
  delay(1);
  LowPinsHigh();
  HighPinsLow();
  digitalWrite(4, HIGH);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  delay(1);
  LowPinsHigh();
  HighPinsLow();
}  
  
  //I
for(j=0; j<=1000; j++)
{
  digitalWrite(2, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(7, LOW);
  digitalWrite(11, LOW);
  delay(1);
  LowPinsHigh();
  HighPinsLow();
  digitalWrite(3, HIGH);
  LowPinsLow();
  delay(1);
  LowPinsHigh();
  HighPinsLow();
  
}  
  //T
for(j=0; j<=1000; j++)
{
  digitalWrite(2, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(7, LOW);
  delay(1);
  LowPinsHigh();
  HighPinsLow();
  digitalWrite(3, HIGH);
  LowPinsLow();
  delay(1);
  LowPinsHigh();
  HighPinsLow();
}
//-
for(j=0; j<=1000; j++)
{
  digitalWrite(2, HIGH);
  digitalWrite(3, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(9, LOW);
  delay(1);
  LowPinsHigh();
  HighPinsLow();
}  
  //U
for(j=0; j<=1000; j++)
{
  digitalWrite(2, HIGH);
  digitalWrite(5, HIGH);
  for(i= 7; i<=10; i++)
    digitalWrite(i, LOW);
  delay(1);
  LowPinsHigh();
  HighPinsLow();
  digitalWrite(3, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(11, LOW);
  delay(1);
  LowPinsHigh();
  HighPinsLow();
}
}
