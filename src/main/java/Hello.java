// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// Import required java libraries
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

// Extend HttpServlet class
public class Hello extends HttpServlet {

  public static String appVersion = "1";
  public static String welcomeMsg = "Welcome to the Hello World App";

   private String message;

   public void init() throws ServletException {
   }

   public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {

      // Set response content type
      response.setContentType("text/html");
      message = "Hello";
      String queryString = request.getQueryString();

      if (queryString != null) {
         message = message + " " + queryString;
      }

      // Actual logic goes here.
      PrintWriter out = response.getWriter();
      out.println("<h1>" + welcomeMsg + " version " + appVersion + "</h1>");
      out.println("<h2>" + message + "</h1>");
   }
}
