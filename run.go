package main

import (
    "log"

    "github.com/gofiber/fiber/v2"
    "github.com/gofiber/fiber/v2/middleware/proxy"
)

func main() {
    app := fiber.New()

    app.Get("/proxy", func(c *fiber.Ctx) error {
        url := c.Query("url")
        if err := proxy.Do(c, url); err != nil {
            return err
        }
        c.Set("Cross-Origin-Resource-Policy", "cross-origin")
        return nil
    })

    log.Fatal(app.Listen(":3000"))
}
