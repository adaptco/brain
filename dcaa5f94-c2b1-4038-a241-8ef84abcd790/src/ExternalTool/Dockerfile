FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY ["ExternalTool.csproj", "./"]
RUN dotnet restore "ExternalTool.csproj"
COPY . .
RUN dotnet publish "ExternalTool.csproj" -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app
COPY --from=build /app/publish .
ENTRYPOINT ["dotnet", "ExternalTool.dll"]
