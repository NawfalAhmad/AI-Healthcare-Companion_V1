import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

const ai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

// MAIN CHAT ROUTE
app.post("/chat", async (req, res) => {
  try {
    const userMsg = req.body.message;

    const completion = await ai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [
        { role: "system", content: "You are a helpful and safe medical assistant. Do NOT diagnose, but give health guidance, precautions, medicines overview, and advise doctor consultation for severe symptoms." },
        { role: "user", content: userMsg }
      ]
    });

    const reply = completion.choices[0].message.content;
    return res.json({ reply });

  } catch (err) {
    console.error(err);
    return res.json({ reply: "Error communicating with AI. Try again." });
  }
});

app.listen(5000, () => console.log("Server running on port 5000"));
