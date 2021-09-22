package com.example.SpringBootSample.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/user")
public class UserListController {
    
    // display user list screen
    @GetMapping("/list")
    public String getUserList(){

        // display user list screen
        return "user/list";
    }

}