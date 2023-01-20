import Head from "next/head";
import Container from "../components/container";
import HeroPost from "../components/hero-post";
import Intro from "../components/intro";
import Layout from "../components/layout";
import MoreStories from "../components/more-stories";
import Post from "../interfaces/post";
import { getAllPosts } from "../lib/api";
import { getAllArticles } from "../lib/python_api";

type Props = {
  allPosts: Post[];
};

export default function Index({ allPosts }: Props) {
  const mainArticle = allPosts[0];
  console.log(mainArticle);
  const moreArticles = allPosts.slice(1);
  return (
    <>
      <Layout>
        <Head>
          <title>Next.js Blog with Python</title>
        </Head>
        <Container>
          <Intro />
          {mainArticle && (
            <HeroPost
              title={mainArticle.title}
              coverImage={mainArticle.coverImage}
              date={mainArticle.date}
              author_name={mainArticle.author_name}
              author_image={mainArticle.author_picture}
            />
          )}
          {moreArticles.length > 0 && <MoreStories posts={moreArticles} />}
        </Container>
      </Layout>
    </>
  );
}

export const getStaticProps = async () => {
  const allArticles = getAllPosts([
    "title",
    "date",
    "slug",
    "author",
    "coverImage",
    "excerpt",
  ]);

  const posts = await getAllArticles();
  console.log(posts);

  return {
    props: { allPosts: posts },
  };
};
