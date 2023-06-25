package com.example.reportapp_java;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

public class ReportActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_report);
        Intent intent = getIntent();
        String loc = intent.getStringExtra("location");
        String[] locArr = loc.split(",");
        TextView tv_latStatus = findViewById(R.id.tv_latStatus);
        TextView tv_lonStatus = findViewById(R.id.tv_lonStatus);
        tv_latStatus.setText(locArr[0]);
        tv_lonStatus.setText(locArr[1]);
        try {
            MqttClient client = new MqttClient("tcp://210.106.192.242:1883", MqttClient.generateClientId(),null);
            client.connect();
            Log.i("Test", "connect");
            client.publish("data", new MqttMessage(loc.getBytes()));
        } catch (MqttException e) {
            e.printStackTrace();
        }
//        findViewById(R.id.btn_send).setOnClickListener(new View.OnClickListener() {//버튼 이벤트 처리
//            @Override
//            public void onClick(View view) {
//
//            }
//        });
    }
}