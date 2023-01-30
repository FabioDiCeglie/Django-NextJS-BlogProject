import axios from "axios";

const url = "https://graphql-backend-django.onrender.com";

export const getAllArticles = async () => {
  const articles = await axios.get("${url}/api/articles");
  return articles.data;
};

export const getArticle = async (id: string) => {
  const post = await axios.get(`${url}/api/articles/${id}`);
  return post.data;
};

export const login = async (username: string, password: string) => {
  const login = await axios.post(`${url}/auth/`, {
    username,
    password,
  });

  return login.data;
};

export const createUser = async (username: string, password: string) => {
  const createUser = await axios.post(`${url}/api/users/`, {
    username,
    password,
  });

  return createUser.data;
};
