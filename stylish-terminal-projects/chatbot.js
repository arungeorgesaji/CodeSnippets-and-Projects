#!/usr/bin/env node

//while running please just package.json type to module so it can work with es6 syntax and not normal require statements

import chalkAnimation from "chalk-animation";
import fetch from "node-fetch"; // Make sure to install 'node-fetch' using npm or yarn
import readline from "readline";
import { createSpinner } from "nanospinner";

const apiKey = "";
const endpoint = "https://api.openai.com/v1/chat/completions";

const sleep_rainbow = (ms = 1500) => new Promise((r) => setTimeout(r, ms));
const sleep_spinner = (ms = 1500) => new Promise((r) => setTimeout(r, ms));

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

async function sendMessage(message) {
  const response = await fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify({
      model: "gpt-3.5-turbo",
      messages: message,
    }),
  });
  const data = await response.json();
  return data.choices[0].message["content"];
}
async function loader() {
  const spinner = createSpinner("generating response").start();
  await sleep_spinner();
  spinner.stop();
}
async function conversationLoop() {
  const conversation = [
    {
      role: "system",
      content:
        "You are a helpful assistant who responds in 1 sentence most of the time,(more only if needed badly).",
    },
  ];

  while (true) {
    const userInput = await new Promise((resolve) => {
      rl.question("You: ", resolve);
    });

    conversation.push({ role: "user", content: userInput });

    const response = await sendMessage(conversation);
    const loading_animation = await loader();

    const rainbowTitle = chalkAnimation.rainbow("'Assistant:'" + response);

    await sleep_rainbow();
    rainbowTitle.stop();
    conversation.push({ role: "assistant", content: response });
  }
}

conversationLoop();
