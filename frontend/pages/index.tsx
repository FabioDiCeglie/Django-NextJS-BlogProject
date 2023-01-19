import Head from "next/head";
import Container from "../components/container";
import HeroPost from "../components/hero-post";
import Intro from "../components/intro";
import Layout from "../components/layout";
import MoreStories from "../components/more-stories";
import Post from "../interfaces/post";
import { getAllPosts } from "../lib/api";

type Props = {
  allPosts: Post[];
};

export default function Index({ allPosts }: Props) {
  const mainArticle = allPosts[0];
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
              author={mainArticle.author}
              slug={mainArticle.slug}
              excerpt={mainArticle.excerpt}
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

  return {
    props: { allPosts: allArticles },
  };
};
