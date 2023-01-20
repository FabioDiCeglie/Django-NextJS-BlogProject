import axios from "axios";

export const getAllArticles = async () => {
  const articles = await axios.get("http://localhost:8000/api/articles");
  return articles.data;
};

export const getArticle = async (id: string) => {
  const post = await axios.get(`http://localhost:8000/api/articles/${id}`);
  return post.data;
};
const headers = {
  "Content-Type": "application/json",
};

export const createUser = async (username: string, password: string) => {
  const createUser = await axios.post(`http://localhost:8000/api/users/`, {
    username,
    password,
  });
  console.log(createUser);
  return createUser;
};
