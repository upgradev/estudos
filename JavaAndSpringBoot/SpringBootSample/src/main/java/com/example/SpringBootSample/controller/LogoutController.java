package com.example.SpringBootSample.controller;

import org.springframework.stereotype.Controller;

import lombok.extern.slf4j.Slf4j;

@Controller
@Slf4j
public class LogoutController {

    // redirect to login screen
    public String postLogout() {
        log.info("Logout");
        return "redirect:/login";
    }

}