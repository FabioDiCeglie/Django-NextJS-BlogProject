import Link from "next/link";
import Post from "../interfaces/post";
import Avatar from "./avatar";
import DateFormatter from "./date-formatter";
import CoverImage from "./cover-image";

type Props = {
  mainArticle: Post;
};

const HeroPost = ({ mainArticle }: Props) => {
  const {
    title,
    date,
    author_picture,
    author_name,
    id,
    coverImage,
    description,
  } = mainArticle;

  return (
    <section>
      <div className="mb-8 md:mb-16">
        <CoverImage title={title} src={coverImage} id={id} />
      </div>
      <div className="md:grid md:grid-cols-2 md:gap-x-16 lg:gap-x-8 mb-20 md:mb-28">
        <div>
          <h3 className="mb-4 text-4xl lg:text-5xl leading-tight">
            <Link
              as={`/posts/${id}`}
              href="/posts/[id]"
              className="hover:underline"
            >
              {title}
            </Link>
          </h3>
          <div className="mb-4 md:mb-0 text-lg">
            <DateFormatter dateString={date} />
          </div>
        </div>
        <div>
          <p className="text-lg leading-relaxed mb-4">{description}</p>
          <Avatar name={author_name} picture={author_picture} />
        </div>
      </div>
    </section>
  );
};

export default HeroPost;
