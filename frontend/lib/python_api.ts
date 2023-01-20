import axios from "axios";

export const getAllArticles = async () => {
  const articles = await axios.get("http://localhost:8000/api/articles");
  return articles.data;
};

export const getArticle = async (id: string) => {
  const post = await axios.get(`http://localhost:8000/api/articles/${id}`);
  return post.data;
};
