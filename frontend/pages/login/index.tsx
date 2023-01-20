import Head from "next/head";
import Container from "../../components/container";
import Layout from "../../components/layout";
import SignIn from "../../components/signIn";
import Link from "next/link";

export default function Index() {
  return (
    <>
      <Layout>
        <Head>
          <title>Log In</title>
        </Head>
        <Container>
          <section className="flex-col md:flex-row flex items-center md:justify-between mt-16 mb-16 md:mb-12">
            <h1 className="text-5xl md:text-8xl font-bold tracking-tighter leading-tight md:pr-6">
              <Link href="/" className="hover:underline">
                Blog.
              </Link>
            </h1>
          </section>
          <SignIn />
        </Container>
      </Layout>
    </>
  );
}
