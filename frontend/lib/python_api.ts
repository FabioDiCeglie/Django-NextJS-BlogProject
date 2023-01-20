import axios from "axios";

export const getAllArticles = async () => {
  const articles = await axios.get("http://localhost:8000/api/articles");
  return articles.data;
};

export const getArticle = async (id: string) => {
  const post = await axios.get(`http://localhost:8000/api/articles/${id}`);
  return post.data;
};

export const login = async (username: string, password: string) => {
  const login = await axios.post(`http://localhost:8000/auth/`, {
    username,
    password,
  });
  return login.data;
};

export const createUser = async (username: string, password: string) => {
  const createUser = await axios.post(`http://localhost:8000/api/users/`, {
    username,
    password,
  });

  return createUser.data;
};
