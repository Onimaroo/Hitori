package com.springdemo.fridayback;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FridayBackController {
    @RequestMapping
    public String Response() {
        return "Petit Test";
    }
}
