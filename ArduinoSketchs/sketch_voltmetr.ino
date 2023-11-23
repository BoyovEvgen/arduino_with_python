void setup() {
  Serial.begin(9600);
}

void loop() {
 
  float voltage = analogRead(A0) * 5 / 1023.0;

  Serial.println(voltage);

  
  delay(500); // Задержка перед повторным измерением
}