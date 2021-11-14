package com.springdemo.fridayback;
import javax.persistence.Id;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;


@Entity
public class Event {
    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    private Long id_event;
    private String description;
    private String location;
    private String start_date;
    private String end_date;

    public Long getId() {
        return id_event;
    }

    public void setId(Long id) {
        this.id_event = id;
    }

    @Override
    public String toString() {
        return String.format(
                "Day[day_name=%ld, description='%s', location='%s']",
                id_event, description, location);
    }

    public String getDescription() {
        return description;
    }

    public String getLocation() {
        return location;
    }

    public String getStart_date() {
        return start_date;
    }

    public String getEnd_date() {
        return end_date;
    }

}
