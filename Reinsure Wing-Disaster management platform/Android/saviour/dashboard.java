package com.aknbinary.saviour;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.Toast;

public class dashboard extends AppCompatActivity {

    private LinearLayout emergency,safe,assistance,news, reg, log;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        emergency=findViewById(R.id.emg);
        safe=findViewById(R.id.safearea);
        assistance=findViewById(R.id.assis);
        news=findViewById(R.id.news);
        reg=findViewById(R.id.reg);
        log=findViewById(R.id.log);

        emergency.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i= new Intent(dashboard.this, MapsActivity.class);
                startActivity(i);


            }
        });

       /* safe.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i= new Intent(dashboard.this, email.class);
                startActivity(i);


            }
        });  */

        assistance.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i= new Intent(dashboard.this, Assistance.class);
                startActivity(i);
            }
        });

        /* news.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i= new Intent(dashboard.this, weather.class);
                startActivity(i);
            }
        }); */
       /* reg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i= new Intent(dashboard.this, weather.class);
                startActivity(i);
            }
        });
        log.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i= new Intent(dashboard.this, weather.class);
                startActivity(i);
            }
        });*/
    }
}
