using Microsoft.AspNetCore.Mvc;
using System.Text.Json;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapPost("/webhook/agent-event", async ([FromBody] JsonElement payload) =>
{
    // 1. Log the incoming event
    var eventType = payload.GetProperty("event_type").GetString();
    var eventKey = payload.GetProperty("event_key").GetString();

    app.Logger.LogInformation($"Received Event: {eventType} [{eventKey}]");

    // 2. Simulate Async Processing (in a real app, queue this)
    // For prototype, we just log and return 200 OK
    await Task.Delay(100);

    // 3. Return accepted status
    return Results.Accepted(value: new { status = "accepted", message = $"Processing started for {eventType}" });
});

app.MapGet("/health", () => Results.Ok("External Tool is Healthy"));

app.Run();
