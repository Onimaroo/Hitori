package com.springdemo.fridayback;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class EventController {
    @Autowired
    private EventRepository repository;

    @GetMapping
    public List<Event> display() {
        return repository.findAll();
    }

    @GetMapping("/event/{id}")
    public Event getEventById(@PathVariable(value = "id") int id) {
        return repository.findById(id);
    }

    @PostMapping("/event")
    @ResponseStatus(HttpStatus.CREATED)
    public Event addEvent(@RequestBody Event event) {
        return repository.save(event);
    }

    @DeleteMapping("/delete/{id}")
    public void deleteEvent(@PathVariable(value = "id") long id) {
        repository.deleteById(id);
    }

}
