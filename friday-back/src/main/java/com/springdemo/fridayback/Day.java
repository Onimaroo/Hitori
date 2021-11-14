package com.springdemo.fridayback;

import javax.persistence.Id;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;

@Entity
public class Day {
    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private String day_name;
    private int number_of_events;
    private boolean holiday_check;

    @Override
    public String toString() {
        return String.format(
                "Day[day_name=%s, number_of_events='%d', holiday_check='%d']",
                day_name, number_of_events, holiday_check);
    }

    public String getDayName() {
        return day_name;
    }

    public int getNumberOfEvents() {
        return number_of_events;
    }

    public boolean getHolidayCheck() {
        return holiday_check;
    }

}
