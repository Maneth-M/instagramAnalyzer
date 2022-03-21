package main

import (
    "log"
    "fmt"
    "github.com/gofiber/fiber/v2"
    "github.com/gofiber/fiber/v2/middleware/proxy"
)

func main() {
    app := fiber.New()

    app.Get("/proxy", func(c *fiber.Ctx) error {
        url := c.Query("url")
        for {
            if err := proxy.Do(c, url); err != nil {
                return err
            }
            if c.Context().Response.StatusCode() != 302 {
                fmt.Println(c.GetRespHeaders()["Location"])
                break
            }
            url = c.GetRespHeaders()["Location"]
        }
        c.Set("Cross-Origin-Resource-Policy", "cross-origin")
        return nil
    })

    log.Fatal(app.Listen(":3000"))
}