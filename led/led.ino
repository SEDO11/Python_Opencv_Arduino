
int arr[5] = {3, 5, 6, 9, 11};

void setup() {
  for(int i=0; i<sizeof(arr); i++){
    pinMode(arr[i], OUTPUT);
  }
}

void loop() {
  for(int i=0; i<sizeof(arr); i++){
    digitalWrite(arr[i], 50);
  }
  delay(1000);
  for(int i=0; i<sizeof(arr); i++){
    digitalWrite(arr[i], LOW);
  }
  delay(1000);

}
