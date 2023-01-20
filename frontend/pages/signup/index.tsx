import Head from "next/head";
import Link from "next/link";
import Container from "../../components/container";
import Layout from "../../components/layout";
import SignUp from "../../components/signup";

export default function Index() {
  return (
    <>
      <Layout>
        <Head>
          <title>Sign Up</title>
        </Head>
        <Container>
          <section className="flex-col md:flex-row flex items-center md:justify-between mt-16 mb-16 md:mb-12">
            <h1 className="text-5xl md:text-8xl font-bold tracking-tighter leading-tight md:pr-8">
              <Link href="/" className="hover:underline">
                Blog.
              </Link>
            </h1>
          </section>
          <SignUp />
        </Container>
      </Layout>
    </>
  );
}
