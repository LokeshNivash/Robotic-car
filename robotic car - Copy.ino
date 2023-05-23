#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <Servo.h>

// Motor driver pins
const int IN1 = D1;
const int IN2 = D2;
const int IN3 = D3;
const int IN4 = D4;
const int ENA = D5;
const int ENB = D6;

// Ultrasonic sensor pins
const int trigPin = D7;
const int echoPin = D8;

// Servo motor pin
const int servoPin = D0;

// WiFi credentials
const char *ssid = "JARVIS";
const char *password = "12345678";

// Web server object
ESP8266WebServer server(80);

// Servo object
Servo servo;
bool isMoving = false;

void setup()
{
  // Initialize serial communication
  Serial.begin(115200);

  // Configure motor driver pins
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  // Configure ultrasonic sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Configure servo motor pin
  servo.attach(servoPin);

  // Connect to WiFi network
  WiFi.mode(WIFI_AP);
  WiFi.softAP(ssid, password);

  // Print the IP address
  Serial.print("Access Point IP address: ");
  Serial.println(WiFi.softAPIP());

  // Start the web server
  server.on("/", handleRoot);
  server.begin();
}

void loop()
{
  server.handleClient();
  if (isMoving)
  {
    moveRobot();
  }
  // rotateServoAndMeasure();
  rotateServoAndMeasure();
}

// Function to handle the root URL
void handleRoot()
{
  if (server.method() == HTTP_POST)
  {
    String command = server.arg("command");
    if (command == "forward")
    {
      // Move forward
      startMoving();
    }
    else if (command == "backward")
    {
      // Move backward
      startMoving();
    }
    else if (command == "left")
    {
      // Turn left
      startMoving();
    }
    else if (command == "right")
    {
      // Turn right
      startMoving();
    }
    else if (command == "stop")
    {
      // Stop
      stopMoving();
    }
  }

  String webpage = "<!DOCTYPE html><html><head><style>"
                   "body { font-family: Arial, Helvetica, sans-serif; text-align: center; }"
                   "h1 { color: #333; }"
                   "button { background-color: #4CAF50; color: white; padding: 10px 20px; "
                   "text-align: center; text-decoration: none; display: inline-block; "
                   "font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 8px; }"
                   "</style></head><body><h1>Robotic Car Control</h1>"
                   "<form method='post'>"
                   "<button type='submit' name='command' value='forward'>Forward</button>"
                   "<br><br>"
                   "<button type='submit' name='command' value='backward'>Backward</button>"
                   "<br><br>"
                   "<button type='submit' name='command' value='left'>Left</button>"
                   "<button type='submit' name='command' value='right'>Right</button>"
                   "<br><br>"
                   "<button type='submit' name='command' value='stop'>Stop</button>"
                   "</form></body></html>";

  server.send(200, "text/html", webpage);
}

// Function to start moving the robot
void startMoving()
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 255);
  analogWrite(ENB, 255);
  isMoving = true;
}

// Function to stop moving the robot
void stopMoving()
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
  isMoving = false;
}

// Function to measure distance using the ultrasonic sensor
float measureDistance()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  float distance = duration * 0.034 / 2;

  return distance;
}

// Function to rotate the servo motor to a specific angle
void rotateServo(int angle)
{
  servo.write(angle);
  delay(500);
}

void rotateServoAndMeasure()
{
  int angles[5] = {0, 45, 90, 135, 180};

  for (int i = 0; i < 5; i++)
  {
    rotateServo(angles[i]);
    delay(500);
    float distance = measureDistance();
    if (distance < 30)
    {
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      digitalWrite(IN3, LOW);
      digitalWrite(IN4, LOW);
      analogWrite(ENA, 0);
      analogWrite(ENB, 0);
      break;
    }
  }
}
void startMovingForward()
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 255);
  analogWrite(ENB, 255);
  isMoving = true;
}

void startMovingBackward()
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  analogWrite(ENA, 255);
  analogWrite(ENB, 255);
  isMoving = true;
}

void startTurningLeft()
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 200);
  analogWrite(ENB, 200);
  isMoving = true;
}

void startTurningRight()
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  analogWrite(ENA, 200);
  analogWrite(ENB, 200);
  isMoving = true;
}
void moveRobot()
{
  // Implement the logic for continuous movement here
  // For example, you can continuously move the robot forward
  // until the stop button is pressed
  servo.write(90);
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 255);
  analogWrite(ENB, 255);
}

void stopFunc()
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
}
