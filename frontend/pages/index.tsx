import Head from "next/head";
import Container from "../components/container";
import HeroPost from "../components/hero-post";
import Intro from "../components/intro";
import Layout from "../components/layout";
import MoreStories from "../components/more-stories";
import Post from "../interfaces/post";
import { getAllArticles } from "../lib/python_api";
type Props = {
  allArticles: Post[];
};

export default function Index({ allArticles }: Props) {
  const mainArticle = allArticles[0];
  const moreArticles = allArticles.slice(1);
  return (
    <>
      <Layout>
        <Head>
          <title>Next.js Blog with Python</title>
        </Head>
        <Container>
          <Intro />
          {mainArticle && <HeroPost mainArticle={mainArticle} />}
          {moreArticles.length > 0 && <MoreStories articles={moreArticles} />}
        </Container>
      </Layout>
    </>
  );
}

export const getStaticProps = async () => {
  const articles = await getAllArticles();

  return {
    props: { allArticles: articles },
  };
};
