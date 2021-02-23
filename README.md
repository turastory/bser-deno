# BSER.FUN API 리뉴얼

## 구조

> Inspired by [Bulletproof node.js project architecture](https://softwareontheroad.com/ideal-nodejs-project-structure/)

3 main components:

- controller
  Deals with routing and parameter validation.
  It works like a bridge between the user and the service.

- service
  Core application logic goes here.

- data
  All sort of data source like DB or 3rd party APIs.

Additional components:

- loader
  Initialization scripts and logic goes here. (Database connection, i18n setup, etc.)

- model
  Data entities that we can use through the whole application.

- scheduler
  Codes that needs to run on a specific period, or a specific time.

## 목표

- Javascript -> Typescript
- Node -> Deno
- Python as a separate application