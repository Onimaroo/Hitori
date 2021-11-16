package com.springdemo.fridayback;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface EventRepository extends CrudRepository<Event, Long> {
    List<Event> findAll();
    List<Event> findByDescription(String description);
    Event findById(long id);
}
