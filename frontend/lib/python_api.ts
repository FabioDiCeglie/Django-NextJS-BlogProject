import axios from "axios";

export const getAllArticles = async () => {
  const posts = await axios.get("http://localhost:8000/api/articles");
  return posts.data;
};

export const getArticle = async (id: string) => {
  const post = await axios.get(`http://localhost:8000/api/articles/${id}`);
  return post.data;
};
