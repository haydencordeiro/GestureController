//sensor 1
const int trigPin1 = 9;
const int echoPin1 = 10;
unsigned long startTime1;
unsigned long restart1;
// defines variables
long duration1;
int distance1;
int count1=0;
int flag1=0;

//sensor 2
const int trigPin2 = 9;
const int echoPin2 = 10;
unsigned long startTime2;
unsigned long restart2;
// defines variables
long duration2;
int distance2;
int count2=0;
int flag2=0;

void setup() {
//sensor 1
pinMode(trigPin1, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin1, INPUT); // Sets the echoPin as an Input
flag1=0;
Serial.begin(9600); // Starts the serial communication
restart1=millis();

//sensor 2
pinMode(trigPin2, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin2, INPUT); // Sets the echoPin as an Input
flag2=0;
Serial.begin(9600); // Starts the serial communication
restart2=millis();


}
void loop() {
//sensor 1
digitalWrite(trigPin1, LOW);
delayMicroseconds(2);
digitalWrite(trigPin1, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin1, LOW);
duration1 = pulseIn(echoPin1, HIGH);
distance1= duration1*0.034/2;


//sensor 2
digitalWrite(trigPin2, LOW);
delayMicroseconds(2);
digitalWrite(trigPin2, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin2, LOW);
duration2 = pulseIn(echoPin2, HIGH);
distance2= duration2*0.034/2;


//logic
if(distance1 <=10 &&( millis()-restart1>1000 && flag1==0)){
startTime1=millis();
flag1=1;

  
}
if(distance2 <=10 &&( millis()-restart2>1000 && flag2==0)){
startTime2=millis();
flag2=1;

  
}

if(flag1==1){
if(millis()-startTime1>1000 && millis()-startTime2>1000 )
{
  if(distance1<=10 && distance2<=10){
  Serial.println(2);
  restart1=millis();
  restart2=millis();
  flag1=0;
  flag2=0;
  
} 
else if(millis()-startTime1>1000)
{
  if(distance1<=10){
  Serial.println(1);
  restart1=millis();
  flag1=0;
  }
  else 
  {
    Serial.println(0);
    flag1=0;
   }
}

}

}
if(flag2==1){
if(millis()-startTime1>1000 && millis()-startTime2>1000 )
{
  if(distance1<=10 && distance2<=10){
  Serial.println(2);
  restart1=millis();
  restart2=millis();
  flag1=0;
  flag2=0;
  
} 
else if(millis()-startTime2>1000)
{
  if(distance2<=10){
  Serial.println(4);
  restart2=millis();
  flag2=0;
  }
  else 
  {
    Serial.println(3);
    flag2=0;
   }
}

}
}



}//loop end
