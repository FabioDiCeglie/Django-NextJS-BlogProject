import axios from "axios";

export const getAllArticles = async () => {
  const posts = await axios.get("http://localhost:8000/api/articles");
  return posts.data;
};
