package main

import (
    "fmt"
    "log"
    "net/url"

    //"fmt"
    "github.com/gofiber/fiber/v2"
    "github.com/gofiber/fiber/v2/middleware/proxy"
)

func main() {
    app := fiber.New()

    app.Get("/proxy", func(c *fiber.Ctx) error {
        uri := c.Query("url")
        if err := proxy.Do(c, uri); err != nil {
            return err
        }
        c.Set("Cross-Origin-Resource-Policy", "cross-origin")
        if c.Context().Response.StatusCode() == 302 {
            uri = c.GetRespHeaders()["Location"]
            c.Set("Location", fmt.Sprintf("/proxy?url=%s", url.QueryEscape(uri)))
        }
        return nil
    })

    log.Fatal(app.Listen(":3000"))
}